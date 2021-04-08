#ifndef ULTRASONIC_CLASS
#define ULTRASONIC_CLASS

#include "BaseClass.h"
#include "MethodDescriptor.h"

class Ultrasonic;

namespace nanpy {

    class GroveUltrasonicClass: public ObjectsManager<Ultrasonic> {

        public:
            void elaborate( nanpy::MethodDescriptor* m );
            const char* get_firmware_id();

    };
}

#endif
