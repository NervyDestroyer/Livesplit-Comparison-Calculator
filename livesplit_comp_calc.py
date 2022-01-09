import argparse
import datetime

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-comp", type=str, default="./comp.txt", help="Path to the comparison txt")
    parser.add_argument("-output", type=str, default="./out.txt", help="Path to the output txt")

    return parser.parse_args()

def main():
    args = parse_args()
    full_comp_time = datetime.time()

    with open(args.comp, "r") as i_stream:
        lines = i_stream.readlines()

    lines = [line.strip() for line in lines]
    lines = [line for line in lines if len(line) != 0]
    lines = [line for line in lines if line[0] != '#']

    comp_at_each_split = []

    # Go through each line and add to comparison
    for line in lines:
        t = datetime.datetime.strptime(line, "%M:%S").time()

        split_delta = datetime.timedelta(minutes=t.minute, seconds=t.second)
        comp_delta = datetime.timedelta( \
            hours=full_comp_time.hour, minutes=full_comp_time.minute, seconds=full_comp_time.second)

        # datetime.datetime.min is to convert the final result into a datetime
        full_comp_time = (comp_delta + split_delta + datetime.datetime.min).time()

        comp_at_each_split.append(full_comp_time)

    # print final time
    print("Final time:", full_comp_time)

    # Write out comparison at each split
    with open(args.output, "w") as o_stream:
        for comp_split in comp_at_each_split:
            o_stream.write("%s\n" % str(comp_split))



if __name__ == "__main__":
    main()
