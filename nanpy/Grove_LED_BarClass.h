#ifndef GROVE_LED_BAR_CLASS
#define GROVE_LED_BAR_CLASS

#include "BaseClass.h"
#include "MethodDescriptor.h"

#include "Grove_LED_Bar.h"

class Grove_LED_Bar;

namespace nanpy {

    class Grove_LED_BarClass: public ObjectsManager<Grove_LED_Bar> {

        public:
            void elaborate( nanpy::MethodDescriptor* m );
            const char* get_firmware_id();

    };
}

#endif

