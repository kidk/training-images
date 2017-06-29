package com.coscale;

import java.util.HashMap;
import java.util.Map;

import junit.framework.TestCase;

/**
 * Unit test for simple App.
 */
public class AppTest  extends TestCase {

    public void testApp() {
        Map<String, Integer> wordOcc = new HashMap<>();
        wordOcc.put("Hello", 10);
        wordOcc.put("World", 4);

        Map<Character, Integer> letterOcc = App.getLetterOccurrences(wordOcc);

        assertEquals(26, letterOcc.keySet().size());
        for (char c : "abcfgijkmnpqstuvxyz".toCharArray()) {
            assertEquals(0, (int) letterOcc.get(c));
        }

        assertEquals(10, (int) letterOcc.get('h'));
        assertEquals(10, (int) letterOcc.get('e'));
        assertEquals(24, (int) letterOcc.get('l'));
        assertEquals(14, (int) letterOcc.get('o'));
        assertEquals(4, (int) letterOcc.get('w'));
        assertEquals(4, (int) letterOcc.get('r'));
        assertEquals(4, (int) letterOcc.get('d'));
    }

}
