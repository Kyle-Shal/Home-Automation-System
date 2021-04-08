/*
 * Copyright (c) 2019-2020 Mahya Soleimani Jadidi
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * * Redistributions of source code must retain the above copyright notice, this
 *   list of conditions and the following disclaimer.
 *
 * * Redistributions in binary form must reproduce the above copyright notice,
 *   this list of conditions and the following disclaimer in the documentation
 *   and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 * OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */


#include "cfg.h"

#if USE_Grove_LED_Bar

#include <Arduino.h>
#include "Grove_LED_Bar.h"
#include "Grove_LED_BarClass.h"
#include <stdlib.h>

const char* nanpy::Grove_LED_BarClass::get_firmware_id()
{
	return "Grove_LED_Bar";
}

void nanpy::Grove_LED_BarClass::elaborate( nanpy::MethodDescriptor* m ) {
	ObjectsManager<Grove_LED_Bar>::elaborate(m);

	if (strcmp(m->getName(),"new") == 0) {
		Grove_LED_Bar * ds;
		ds = new Grove_LED_Bar(m->getInt(0), m->getInt(1), m->getBool(2));
		ds->begin();
		v.insert(ds);
		m->returns(v.getLastIndex());
	}


	if (strcmp(m->getName(), "setLevel") == 0) {
		v[m->getObjectId()]->setLevel(m->getFloat(0));
		m->returns(0);
	}

};
#endif
