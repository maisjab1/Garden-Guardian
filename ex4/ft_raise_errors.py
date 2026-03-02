#!/usr/bin/env python3

def check_plant_health(
    plant_name: str, water_level: int, sunlight_hours: int
) -> None:
    try:
        if not plant_name:
            raise ValueError("Plant name cannot be empty")
        if not (1 < water_level):
            raise ValueError(
                f"Water level {water_level} is too low (min 1)"
            )
        if not (water_level < 10):
            raise ValueError(
                f"Water level {water_level} is too high (max 10)"
            )
        if not (2 < sunlight_hours):
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)"
            )
        if not (sunlight_hours < 12):
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)"
            )
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    check_plant_health("tomato", 2, 5)
    print("\nTesting empty plant name...")
    check_plant_health(None, 2, 5)
    print("\nTesting bad water level...")
    check_plant_health("tomato", 15, 5)
    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 2, 0)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
