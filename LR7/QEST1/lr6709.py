import pydoc

description = pydoc.render_doc(pow, "Help on %s")
print(description)
