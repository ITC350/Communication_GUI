import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

window = Gtk.Window(title="Hello World")

hbox = Gtk.Box(spacing=6)
window.add(hbox)

button = Gtk.Button.new_with_label("Click Me")
hbox.pack_start(button, True, True, 0)

button2 = Gtk.Button.new_with_label("Click Me Too")
hbox.pack_start(button2, True, True, 1)

window.show()
window.show_all()
window.connect("destroy", Gtk.main_quit)
Gtk.main()

