def temperature_correction(temperature):
    base_growth_rate = 1.0  # 基本の生育速度
    max_temperature = 29.0  # 29℃以上の気温

    if temperature <= max_temperature:
        return temperature  # 29℃以下の場合、補正なし

    # 29℃以上の場合、指数関数による補正
    correction_factor = 3.0 ** ((max_temperature - temperature) / 5.0)
    corrected_temperature = temperature * correction_factor
    #corrected_temperature = 0

    return corrected_temperature