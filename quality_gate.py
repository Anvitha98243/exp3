
MINIMUM_ACCURACY = 0.80


def check_model_quality(accuracy):
    print("Model accuracy:", round(accuracy * 100, 2), "%")
    print("Minimum required accuracy:", MINIMUM_ACCURACY * 100, "%")

    if accuracy >= MINIMUM_ACCURACY:
        print("QUALITY GATE PASSED")
        return True
    else:
        print("QUALITY GATE FAILED")
        return False


if __name__ == "__main__":
    model_accuracy = 0.85

    if not check_model_quality(model_accuracy):
        raise SystemExit(1)
