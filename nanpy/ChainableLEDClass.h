#ifndef CHAINABLELED_CLASS
#define CHAINABLELED_CLASS

#include "BaseClass.h"
#include "MethodDescriptor.h"

#include "ChainableLED.h"

class ChainableLED;

namespace nanpy {

    class ChainableLEDClass: public ObjectsManager<ChainableLED> {

        public:
            void elaborate( nanpy::MethodDescriptor* m );
            const char* get_firmware_id();

    };
}

#endif
