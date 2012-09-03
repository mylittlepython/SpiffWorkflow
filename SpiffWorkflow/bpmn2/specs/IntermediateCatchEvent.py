from SpiffWorkflow.Task import Task
from SpiffWorkflow.bpmn2.specs.BpmnSpecMixin import BpmnSpecMixin
from SpiffWorkflow.specs.Simple import Simple

__author__ = 'matth'

class IntermediateCatchEvent(Simple, BpmnSpecMixin):

    def __init__(self, parent, name, event_spec, **kwargs):
        super(IntermediateCatchEvent, self).__init__(parent, name, **kwargs)
        self.event_spec = event_spec


    def _update_state_hook(self, my_task):
        if self.event_spec.has_fired(my_task):
            return super(IntermediateCatchEvent, self)._update_state_hook(my_task)
        else:
            my_task._set_state(Task.WAITING)
            return False

    def accept_message(self, my_task, message):
        if my_task.state == Task.WAITING and self.event_spec.accept_message(my_task, message):
            self._update_state(my_task)
            return True
        return False