import vpic_client


if __name__ == "__main__":
    result = vpic_client.get_vin_record("1FUJGLDR3HLHG7532")
    print(result)