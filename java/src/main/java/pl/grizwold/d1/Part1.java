package pl.grizwold.d1;

import java.util.List;

public class Part1 {
    int calculateFrequencies(List<String> changes) {
        return changes.stream()
                .map(Integer::parseInt)
                .reduce((acc, i) -> acc + i)
                .orElse(0);
    }
}