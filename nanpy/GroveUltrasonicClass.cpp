#include "cfg.h"

#if USE_Grove_Ultrasonic

#include <Arduino.h>
#include "Ultrasonic.h"
#include "GroveUltrasonicClass.h"
#include <stdlib.h>

const char* nanpy::GroveUltrasonicClass::get_firmware_id()
{
    return "Ultrasonic";
}

void nanpy::GroveUltrasonicClass::elaborate( nanpy::MethodDescriptor* m ) {
        ObjectsManager<Ultrasonic>::elaborate(m);

        if (strcmp(m->getName(),"new") == 0) {
            Ultrasonic * sensor;
			sensor = new Ultrasonic(m->getInt(0));
			v.insert(sensor);
            m->returns(v.getLastIndex());
        }

        if (strcmp(m->getName(), "MeasureInCentimeters") == 0) {
            m->returns(v[m->getObjectId()]->MeasureInCentimeters());
        }
};
#endif
