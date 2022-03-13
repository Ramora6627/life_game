from gameoflife import width, height, stage, print_stage, count_neighbors

def init_stage(stage):
    for v_pos in range(0, height):
      for h_pos in range(0, width):
        if h_pos == 1:
          stage[v_pos][h_pos] = True
        else:
          stage[v_pos][h_pos] = False
    # print (stage)
    return stage

# Generation Rules:
# 1. Any live cell with < 2 neighbors dies
# 2. Any live cell with 2-3 neighbors lives
# 3. Any live cell with > 3 neighbors dies
# 4. Any dead cell with 3 neighbors comes alive
def continue_stage(stage):
    for v_pos in range(0, height):
      for h_pos in range(0, width):
        if h_pos == 1:
          stage[v_pos][h_pos] = True
        else:
          stage[v_pos][h_pos] = False
    # print (stage)
    return stage
def get_neighbors_grid(stage):
    neighbor_num = {}
    for v_pos in range(len(stage)):
        for h_pos in range(len(stage[v_pos])):
            neighbors = count_neighbors(stage, v_pos, h_pos)
            neighbor_num[(v_pos+1,h_pos+1)]= neighbors
            # print (f"row{v_pos+1} and column {h_pos+1} has {neighbors} neighbors")
    print (neighbor_num)
    return (neighbor_num)
def one_generation(stage):
    neighbor_num = get_neighbors_grid(stage)
    
    for v_pos in range(len(stage)):
        for h_pos in range(len(stage[v_pos])):
          if not stage[v_pos][h_pos] and neighbor_num[v_pos+1,h_pos+1] == 3:
            stage[v_pos][h_pos] = True
                # print (stage[v_pos][h_pos])
          elif stage[v_pos][h_pos] and neighbor_num[v_pos+1,h_pos+1] < 2:
            stage[v_pos][h_pos] = False
          elif stage[v_pos][h_pos] and (neighbor_num[v_pos+1,h_pos+1] == 2 or neighbor_num[v_pos+1,h_pos+1] == 3):
            stage[v_pos][h_pos] = True
          elif stage[v_pos][h_pos] and neighbor_num[v_pos] > 3:
            stage[v_pos][h_pos] = False

    # print (stage)
                

init_stage(stage)
print("First Generation:")
print_stage(stage)
get_neighbors_grid(stage)
one_generation(stage)
print("Second Generation:")
print_stage(stage)

