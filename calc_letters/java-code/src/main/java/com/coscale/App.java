package com.coscale;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.HashMap;
import java.util.Map;

import redis.clients.jedis.Jedis;

/**
 * calc-letters reads all words from a MySQL database and stores the letter
 * count in a Redis database.
 */
public class App {

    public static void main(String[] args) throws ClassNotFoundException, SQLException {
        String dbHost = System.getenv("DATABASE_HOST");
        String dbUser = System.getenv("DATABASE_USER");
        String dbPass = System.getenv("DATABASE_PASS");
        String db = System.getenv("DATABASE_TABLE");
        String redisHost = System.getenv("REDIS_HOST");
        String loop = System.getenv("LOOP");

        Connection dbConnection = DriverManager.getConnection(
                String.format("jdbc:mysql://%s:3306/%s", dbHost, db), dbUser, dbPass);

        Jedis jedis = new Jedis(redisHost);

        if (loop != null && loop.toLowerCase().equals("true")) {
            while(true) {
                calcLetters(dbConnection, jedis);
                sleepSec(60);
            }
        } else {
            calcLetters(dbConnection, jedis);
        }

        jedis.close();
        dbConnection.close();
    }

    private static void calcLetters(Connection dbConnection, Jedis jedis) throws SQLException {
        Map<String, Integer> wordOccurences = getWordOccurences(dbConnection);
        Map<Character, Integer> letterOccurences = getLetterOccurrences(wordOccurences);

        for (char c : letterOccurences.keySet()) {
            Integer occurences = letterOccurences.get(c);
            System.out.println(String.format("Setting letter %s to %d", c, occurences));
            jedis.set("alfa" + c, occurences.toString());
        }
    }

    private static Map<String, Integer> getWordOccurences(Connection dbConnection) throws SQLException {
        Map<String, Integer> wordOccurences = new HashMap<String, Integer>();

        Statement statement = dbConnection.createStatement();
        ResultSet rs = statement.executeQuery("SELECT word, number FROM words");

        while (rs.next()) {
            String word = rs.getString("word");
            int number = rs.getInt("number");

            if (word != null) {
                if (wordOccurences.containsKey(word)) {
                    wordOccurences.put(word, wordOccurences.get(word) + number);
                } else {
                    wordOccurences.put(word, number);
                }
            }
        }

        statement.close();

        return wordOccurences;
    }

    public static Map<Character, Integer> getLetterOccurrences(Map<String, Integer> wordOccurences) {
        Map<Character, Integer> letterOccurences = new HashMap<>();

        for (char c : "abcdefghijklmnopqrstuvwxyz".toCharArray()) {
            letterOccurences.put(c, 0);
        }

        for (String word : wordOccurences.keySet()) {
            int occurrences = wordOccurences.get(word);
            System.out.println(String.format("Processing word: %s (%d)", word, occurrences));
            for (char c : word.toLowerCase().toCharArray()) {
                if (letterOccurences.containsKey(c)) {
                    letterOccurences.put(c, letterOccurences.get(c) + occurrences);
                }
            }
        }

        return letterOccurences;
    }

    private static void sleepSec(int i) {
        try {
            Thread.sleep(60000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

}
