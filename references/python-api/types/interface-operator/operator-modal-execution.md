# bpy.types.Operator: Modal Execution

### Modal Execution 

This operator supplies an Operator.modal function that keeps getting run to process events until it returns {'FINISHED'} or {'CANCELLED'} .

A modal operator fires each time a fresh event arrives, like a mouse click or a key press; when nothing new comes in, it stays idle. They shine in interactive tools, where the operator can hold its own state and let keys flip options while it runs. Grab, Rotate, Scale, and Fly-Mode are all modal operators.

Operator.invoke kicks the operator into its active state by returning {'`RUNNING_MODAL`'} , which starts the modal loop.

Observe that __init__() and __del__() are declared. They aren't worth much for other operator kinds, but for modal operators they run before Operator.invoke and again once the operator wraps up. The class construction and destruction section has more on this.

The complete program is in the [upstream source](https://docs.blender.org/api/5.1/bpy.types.Operator.html#modal-execution).

[Related references](INDEX.md).
