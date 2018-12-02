package pl.grizwold.d1;

import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Part2Test {

    @Test
    public void example1() {
        List<String> changes = Arrays.asList("+1", "-2", "+3", "+1");
        int total = new Part2().findDuplicatedFrequency(changes);
        assertEquals(total, 2);
    }

    @Test
    public void example2() {
        List<String> changes = Arrays.asList("+1", "-1");
        int total = new Part2().findDuplicatedFrequency(changes);
        assertEquals(total, 0);
    }

    @Test
    public void example3() {
        List<String> changes = Arrays.asList("+3", "+3", "+4", "-2", "-4");
        int total = new Part2().findDuplicatedFrequency(changes);
        assertEquals(total, 10);
    }

    @Test
    public void example4() {
        List<String> changes = Arrays.asList("-6", "+3", "+8", "+5", "-6");
        int total = new Part2().findDuplicatedFrequency(changes);
        assertEquals(total, 5);
    }

    @Test
    public void example5() {
        List<String> changes = Arrays.asList("+7", "+7", "-2", "-7", "-4");
        int total = new Part2().findDuplicatedFrequency(changes);
        assertEquals(total, 14);
    }

    @Test
    public void solution() throws IOException, URISyntaxException {
        List<String> changes = loadFile("d1_input.txt");
        int total = new Part2().findDuplicatedFrequency(changes);
        System.out.println(total);
    }

    private List<String> loadFile(String filename) throws IOException, URISyntaxException {
        return Files.lines(Paths.get(getClass().getClassLoader().getResource(filename).toURI())).collect(Collectors.toList());
    }
}