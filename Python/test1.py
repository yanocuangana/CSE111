import math



def main ():
    can_name = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3",
"#5", "#6Z", "#8Z short", "#10", "#211", "#300","#303"]

    can_radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.4, 6.83, 15.72, 6.83, 7.62, 8.1]

    can_height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29,8.89, 7.62, 17.78, 12.38, 11.27, 11.11]

    can_cost = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]
    for i in range(len(can_name)):
        name = can_name[i]
        radius = can_radius[i]
        height = can_height[i]
        cost = can_cost[i]
        print(f"{name} {compute_storage_efficiency(radius, height):.2f}")  # type: ignore


def compute_volume (radius, height):
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area (radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency (radius, height):
    storage_efficiency = compute_volume(radius,height)/compute_surface_area(radius, height)
    return storage_efficiency

main()