#pragma once

#include "esphome.h"
#include "esphome/components/sensor/sensor.h"
#include "zmpt101b.h"

#define SENSITIVITY 509.0f

namespace esphome {
namespace zmpt101b_ns {

class ZMPT101BSensor : public PollingComponent, public sensor::Sensor {
 public:
  uint8_t adcPin;
  esphome::zmpt101b_ns::ZMPT101B *zmpt101b;
  // constructor
  ZMPT101BSensor(uint8_t adcPin) : PollingComponent(1000) {
    this->adcPin = adcPin;
    this->zmpt101b = new esphome::zmpt101b_ns::ZMPT101B(adcPin);
  }

  float get_setup_priority() const override { return esphome::setup_priority::HARDWARE; }

  void setup() override {
    this->zmpt101b->setSensitivity(SENSITIVITY);
  }

  void update() override {
    float Vrms = this->zmpt101b->getRmsVoltage();
    publish_state(Vrms);
  }
};

}
}
