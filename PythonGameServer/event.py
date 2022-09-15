## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <_boost_func_of_void/intrusive_ptr.hpp>

class event_info_data:
    def __init__(self):
        pass
    def close(self):
        pass
class TEVENTFUNC:
    def invoke(self, event, processing_time):
        pass



## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define EVENTFUNC(name) long (name) (LPEVENT event, long processing_time)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define EVENTINFO(name) struct name : public event_info_data

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#struct TQueueElement

class event:
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.func = TEVENTFUNC()
        self.info = []
        self.q_el = None
        self.is_force_to_end = '\0'
        self.is_processing = '\0'
        self.ref_count = size_t()

        self.func = TEVENTFUNC(None)
        self.info = event_info_data(None)
        self.q_el = None
        self.ref_count = 0
    def close(self):
        if self.info is not None:
            LG_DEL_MEM(self.info)
