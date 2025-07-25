#pragma once

#include <stdint.h>
#include <Arduino.h>

#define DEFAULT_FREQUENCY 60.0f
#define DEFAULT_SENSITIVITY 500.0f

#if defined(AVR)
	#define ADC_SCALE 1023.0f
	#define VREF 5.0f
#elif defined(ESP8266)
	#define ADC_SCALE 1023.0
	#define VREF 3.3
#elif defined(ESP32)
	#define ADC_SCALE 4095.0
	#define VREF 3.3
#endif

namespace esphome {
namespace zmpt101b_ns {

class ZMPT101B
{
public:
	ZMPT101B (uint8_t pin, uint16_t frequency = DEFAULT_FREQUENCY);
	void     setSensitivity(float value);
	float 	 getRmsVoltage(uint8_t loopCount = 1);

private:
	uint8_t  pin;
	uint32_t period;
	float 	 sensitivity = DEFAULT_SENSITIVITY;
	int 	 getZeroPoint();
};

}
}
