def extract_clinical_markers(tests):
    markers = {}

    for test in tests:
        test_name = test.test_type.lower()

        if test_name == "troponin":
            markers["troponin"] = test.value

        elif test_name == "blood_pressure":
            markers["blood_pressure"] = test.value

        elif test_name == "ecg":
            markers["ecg"] = test.value

    return markers
