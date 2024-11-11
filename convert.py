def str_to_float(num:str)->float or None:
    try:
        return float(num)
    except ValueError:
        return None