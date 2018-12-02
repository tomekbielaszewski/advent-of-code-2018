package pl.grizwold.d1;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Part2 {
    int findDuplicatedFrequency(List<String> changes) {
        int total = 0;
        Set<Integer> alreadySeen = new HashSet<>();
        int size = changes.size();
        int counter  = 0;

        do {
            alreadySeen.add(total);
            int change = Integer.parseInt(changes.get(counter));
            total += change;
            counter++;
            counter = counter >= size ? 0 : counter;
        } while (!alreadySeen.contains(total));

        return total;
    }
}
