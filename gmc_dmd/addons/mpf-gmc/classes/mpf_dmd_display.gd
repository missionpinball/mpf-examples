class_name MPFDMDDisplay
extends MPFDisplay

var is_done := false
@export var resolution: Vector2i

func _ready() -> void:
	super()
	if not resolution:
		var dims = self.get_viewport_rect()
		resolution = Vector2i(dims.size.x, dims.size.y)
	print("I am a GMC DMD HAHA: %s" % resolution)
	RenderingServer.frame_pre_draw.connect(self._pre_draw)
	# RenderingServer.frame_post_draw.connect(self._post_draw)
	print("forcing additional output")
	DisplayServer.register_additional_output(self)

func _exit_tree() -> void:
	DisplayServer.unregister_additional_output(self)

func _pre_draw():
	if RenderingServer.has_changed():
		# is_done = false
		print(" - draw is changed?")
		await RenderingServer.frame_post_draw
		self._capture()
		print(" - draw is done?")

# func _post_draw() -> void:
# 	if RenderingServer.has_changed():
# 	if not is_done:
# 		is_done = true

func _capture() -> void:
	var tex := get_viewport().get_texture().get_image()
	tex.crop(resolution.x, resolution.y)
	var color = tex.get_pixelv(Vector2i(0, 0))
	print("Pixel at 0, 0 is %s " % color)
	var data = tex.get_data()
	# print("RAW DATA: %s" % tex.get_data())
	print("Data is %s bytes?" % data.size())
	if not MPF.server._client:
		print("no client")
		return
	# MPF.server.send_event_with_args("rgb_dmd_frame", {"rawbytes": data, "name": self.name})
	MPF.server.send_event("rgb_dmd_frame&bytes=%d" % data.size())
	MPF.server._client.put_data(data)
	# MPF.server._client.put_data("\n".to_ascii_buffer())
