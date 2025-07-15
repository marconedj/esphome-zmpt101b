import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_ID,
    CONF_PIN,
    CONF_VOLTAGE,
    DEVICE_CLASS_VOLTAGE,
    STATE_CLASS_MEASUREMENT,
    UNIT_VOLT,
    ICON_FLASH,
)
sensor_ns = cg.esphome_ns.namespace('zmpt101b_ns')

Zmpt101bSensor = sensor_ns.class_('ZMPT101BSensor', cg.PollingComponent)

CONFIG_SCHEMA = (
    sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        icon=ICON_FLASH,
        accuracy_decimals=2,
        state_class=STATE_CLASS_MEASUREMENT,
        device_class=DEVICE_CLASS_VOLTAGE,
    )
    .extend(
        {
            cv.GenerateID(): cv.declare_id(Zmpt101b),
            cv.Required(CONF_PIN): pins.internal_gpio_input_pin_schema,
            cv.Optional(CONF_VOLTAGE, default="3.3"): cv.string,
        }
    )
    .extend(cv.polling_component_schema("60s"))
)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID], config["adc_pin"], config["sensitivity"])
    yield cg.register_component(var, config)
    yield sensor.register_sensor(var, config)
