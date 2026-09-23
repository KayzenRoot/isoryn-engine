extends Node3D
# ISORYN-WO-0002 deterministic measurement harness (evidence tooling, not engine code).
#
# It builds one fixed scene from a constant seed, warms up, then reports per-frame CPU wall
# time percentiles plus the engine's own Performance monitors as a single JSON line prefixed
# with ISORYN_BENCH, and quits. No input, no audio, no random clock, no network: the only
# source of variation is the machine and the build under test.

const WARMUP_FRAMES := 90
const MEASURE_FRAMES := 600
const INSTANCE_COUNT := 1200
const GRID_COLUMNS := 40
const SPACING := 3.0
const RNG_SEED := 20260923
const YAW_STEP := 0.0025

var frames_us := []
var last_us := 0
var phase := "warmup"
var phase_count := 0
var started_us := 0


func _ready() -> void:
	started_us = Time.get_ticks_usec()

	var camera := Camera3D.new()
	add_child(camera)
	camera.position = Vector3(0.0, 42.0, 64.0)
	camera.rotation_degrees = Vector3(-32.0, 0.0, 0.0)
	camera.current = true

	var sun := DirectionalLight3D.new()
	add_child(sun)
	sun.rotation_degrees = Vector3(-55.0, 35.0, 0.0)
	sun.shadow_enabled = true

	var box := BoxMesh.new()
	box.size = Vector3(1.6, 1.6, 1.6)

	var surface_mat := StandardMaterial3D.new()
	surface_mat.albedo_color = Color(0.55, 0.5, 0.45)
	surface_mat.roughness = 0.7

	var rng := RandomNumberGenerator.new()
	rng.seed = RNG_SEED
	for i in INSTANCE_COUNT:
		var instance := MeshInstance3D.new()
		instance.mesh = box
		instance.material_override = surface_mat
		var column := float(i % GRID_COLUMNS)
		var row := float(i / GRID_COLUMNS)
		instance.position = Vector3(
			(column - float(GRID_COLUMNS - 1) * 0.5) * SPACING,
			rng.randf_range(0.0, 6.0),
			row * SPACING
		)
		instance.rotation_degrees = Vector3(0.0, rng.randf_range(0.0, 360.0), 0.0)
		add_child(instance)

	last_us = Time.get_ticks_usec()
	print("ISORYN_BENCH_CONFIG " + JSON.stringify({
		"harness": "isoryn-wo-0002-bench",
		"engine_version": Engine.get_version_info().get("string", "unknown"),
		"rendering_method": RenderingServer.get_current_rendering_method(),
		"display_server": DisplayServer.get_name(),
		"window_size": str(get_window().size),
		"instances": INSTANCE_COUNT,
		"seed": RNG_SEED,
		"warmup_frames": WARMUP_FRAMES,
		"measure_frames": MEASURE_FRAMES,
		"ready_us": last_us - started_us,
	}))


func _process(_delta: float) -> void:
	var now := Time.get_ticks_usec()
	if phase == "warmup":
		phase_count += 1
		last_us = now
		if phase_count >= WARMUP_FRAMES:
			phase = "measure"
			phase_count = 0
		return
	frames_us.append(now - last_us)
	last_us = now
	rotation.y += YAW_STEP
	phase_count += 1
	if phase_count >= MEASURE_FRAMES:
		_report()
		get_tree().quit()


func _report() -> void:
	var sorted_frames := frames_us.duplicate()
	sorted_frames.sort()
	var total_us := 0
	for value in frames_us:
		total_us += value
	print("ISORYN_BENCH " + JSON.stringify({
		"harness": "isoryn-wo-0002-bench",
		"engine_version": Engine.get_version_info().get("string", "unknown"),
		"rendering_method": RenderingServer.get_current_rendering_method(),
		"display_server": DisplayServer.get_name(),
		"frames_measured": sorted_frames.size(),
		"frames_drawn": Engine.get_frames_drawn(),
		"mean_frame_ms": float(total_us) / float(sorted_frames.size()) / 1000.0,
		"frame_ms_p50": _percentile_ms(sorted_frames, 0.50),
		"frame_ms_p95": _percentile_ms(sorted_frames, 0.95),
		"frame_ms_p99": _percentile_ms(sorted_frames, 0.99),
		"frame_ms_max": float(sorted_frames[sorted_frames.size() - 1]) / 1000.0,
		"monitors": {
			"time_fps": Performance.get_monitor(Performance.TIME_FPS),
			"time_process_ms": Performance.get_monitor(Performance.TIME_PROCESS),
			"time_physics_process_ms": Performance.get_monitor(Performance.TIME_PHYSICS_PROCESS),
			"memory_static": Performance.get_monitor(Performance.MEMORY_STATIC),
			"object_count": Performance.get_monitor(Performance.OBJECT_COUNT),
			"object_resource_count": Performance.get_monitor(Performance.OBJECT_RESOURCE_COUNT),
			"object_node_count": Performance.get_monitor(Performance.OBJECT_NODE_COUNT),
			"object_orphan_node_count": Performance.get_monitor(Performance.OBJECT_ORPHAN_NODE_COUNT),
			"render_total_objects_in_frame": Performance.get_monitor(Performance.RENDER_TOTAL_OBJECTS_IN_FRAME),
			"render_total_primitives_in_frame": Performance.get_monitor(Performance.RENDER_TOTAL_PRIMITIVES_IN_FRAME),
			"render_total_draw_calls_in_frame": Performance.get_monitor(Performance.RENDER_TOTAL_DRAW_CALLS_IN_FRAME),
			"render_video_mem_used": Performance.get_monitor(Performance.RENDER_VIDEO_MEM_USED),
			"render_texture_mem_used": Performance.get_monitor(Performance.RENDER_TEXTURE_MEM_USED),
			"render_buffer_mem_used": Performance.get_monitor(Performance.RENDER_BUFFER_MEM_USED),
		},
	}))


func _percentile_ms(p_sorted: Array, p_fraction: float) -> float:
	if p_sorted.is_empty():
		return -1.0
	var index := int(round(p_fraction * float(p_sorted.size() - 1)))
	return float(p_sorted[index]) / 1000.0
