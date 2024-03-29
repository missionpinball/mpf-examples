extends MPFSlide

func _ready() -> void:
    $message.visible = false

func show_text(settings: Dictionary, kwargs: Dictionary = {}) -> void:
    print(settings)
    print(kwargs)
    $message.text = settings.tokens.text
    $message.visible = true
