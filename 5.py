from util import read_lines

import apache_beam as beam
from math import copysign


def map_points(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2

    stride = int(copysign(1, x2 - x1))

    if x1 != x2:
        x2 += stride
    xrange = [x for x in range(x1, x2, stride)]
    stride = int(copysign(1, y2 - y1))

    if y1 != y2:
        y2 += stride
    yrange = [y for y in range(y1, y2, stride)]

    if len(xrange) == 0:
        xrange = [x1 for x in range(len(yrange))]

    if len(yrange) == 0:
        yrange = [y1 for x in range(len(xrange))]

    return [p for p in zip(xrange, yrange)]


def make_point(line):
    return (
        (int(line.split()[0].split(",")[0]), int(line.split()[0].split(",")[1])),
        (int(line.split()[2].split(",")[0]), int(line.split()[2].split(",")[1])),
    )


def one(lines):
    with beam.Pipeline() as p:
        (
            p
            | "input" >> beam.Create(lines)
            | "make points" >> beam.Map(make_point)
            | "filter diagonals"
            >> beam.Filter(lambda pt: pt[0][0] == pt[1][0] or pt[0][1] == pt[1][1])
            | "flatmap line points" >> beam.FlatMapTuple(map_points)
            | "count overlaps" >> beam.combiners.Count.PerElement()
            | "key on counts" >> beam.KvSwap()
            | "filter out ones" >> beam.Filter(lambda pair: pair[0] > 1)
            | "count" >> beam.combiners.Count.Globally()
            | "printit!" >> beam.Map(print)
        )


def two(lines):
    with beam.Pipeline() as p:
        (
            p
            | "input" >> beam.Create(lines)
            | "make points" >> beam.Map(make_point)
            | "flatmap line points" >> beam.FlatMapTuple(map_points)
            | "count overlaps" >> beam.combiners.Count.PerElement()
            | "key on counts" >> beam.KvSwap()
            | "filter out ones" >> beam.Filter(lambda pair: pair[0] > 1)
            | "count" >> beam.combiners.Count.Globally()
            | "printit!" >> beam.Map(print)
        )


if __name__ == "__main__":
    lines = read_lines("input-5.txt")
    one(lines)
    two(lines)
