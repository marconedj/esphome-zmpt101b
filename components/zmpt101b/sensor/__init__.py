import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID

sensor_ns = cg.esphome_ns.namespace('zmpt101b_ns')

Zmpt101bSensor = sensor_ns.class_('ZMPT101BSensor', cg.PollingComponent)

CONFIG_SCHEMA = sensor.SENSOR_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(Zmpt101bSensor),
    cv.Required("adc_pin"): cv.int_range(min=0, max=99),
})

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID], config["adc_pin"])
    yield cg.register_component(var, config)
    yield sensor.register_sensor(var, config)
