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

public class Part1Test {

    @Test
    public void example1() {
        List<String> changes = Arrays.asList("+1", "-2", "+3", "+1");
        int total = new Part1().calculateFrequencies(changes);
        assertEquals(total, 3);
    }

    @Test
    public void example2() {
        List<String> changes = Arrays.asList("+1", "+1", "+1");
        int total = new Part1().calculateFrequencies(changes);
        assertEquals(total, 3);
    }

    @Test
    public void example3() {
        List<String> changes = Arrays.asList("+1", "+1", "-2");
        int total = new Part1().calculateFrequencies(changes);
        assertEquals(total, 0);
    }

    @Test
    public void example4() {
        List<String> changes = Arrays.asList("-1", "-2", "-3");
        int total = new Part1().calculateFrequencies(changes);
        assertEquals(total, -6);
    }

    @Test
    public void solution() throws IOException, URISyntaxException {
        List<String> changes = loadFile("d1_input.txt");
        int total = new Part1().calculateFrequencies(changes);
        System.out.println(total);
    }

    private List<String> loadFile(String filename) throws IOException, URISyntaxException {
        return Files.lines(Paths.get(getClass().getClassLoader().getResource(filename).toURI())).collect(Collectors.toList());
    }
}