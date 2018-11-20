package idwall.desafio.string;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by Rodrigo Catão Araujo on 06/02/2018.
 */
public class IdwallFormatter extends StringFormatter {

    public IdwallFormatter(Integer limit, Boolean justify) {
        super(limit, justify);
    }

    /**
     * Formats text, for the lines to meet the column cap and justify as defined
     * in the object instantiation.
     *
     * @param text Text to be formatted.
     * @return Formatted text.
     */
    @Override
    public String format(String text) {
        List<String> lines = this.getFormattedLines(text);
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < lines.size(); ++i) {
            String line;
            if (this.justify == true) {
                line = justifyLine(lines.get(i));
            } else {
                line = lines.get(i);
            }
            sb.append(line + "\n");
        }

        return sb.toString();
    }

    /**
     * Justify a line that has only 1 word or its length less than the specified
     * limit.
     *
     * @param line Line to be justified.
     * @return Justified line.
     */
    private String justifyLine(String line) {
        // calculates extra spaces to add and build the correspondent string
        // based on it
        String[] words = line.split(" ");

        if (words.length == 1) {
            return words[0];
        }

        // `spaces` is the number of spaces between words.
        // also, until the word of index `extraSpaceIndex`, there should
        // be 1 additional space.
        int spaces = 1 + (this.limit - line.length()) / (words.length - 1);
        int extraSpaceIndex =
            (this.limit - line.length()) % (words.length - 1);

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < words.length - 1; ++i) {
            // for each word, append it to the string builder, then
            // append `spaces` or `spaces + 1` whitespaces.
            sb.append(words[i]);

            int currentSpaces = spaces;
            if (i < extraSpaceIndex) {
                ++currentSpaces;
            }
            for (int j = 0; j < currentSpaces; ++j) {
                sb.append(' ');
            }
        }
        sb.append(words[words.length - 1]);
        return sb.toString();
    }

    /**
     * Format lines (without justify) and return them in a list of lines.
     *
     * @param text Text to be formatted
     * @return List of already formatted lines
     */
    private List<String> getFormattedLines(String text) {

        List<String> lines = new ArrayList<String>();

        // The regexp below splits the words separated by whitespace, but keeps
        // the "\n" split as a single word.
        // "Hello\n\n  World" would result in a ["Hello", "\n", "\n", "World"].
        String[] words = text.split(" |((?<=\n)|(?=\n))");

        StringBuilder sb = new StringBuilder();
        int lineLength = 0;
        for (String w : words) {
            if (w.equals("\n")) {
                // when "\n", add the current built string to the list and reset
                lines.add(sb.toString());
                sb.setLength(0);
                lineLength = 0;
            }
            else if (lineLength == 0) {
                // beginning of line
                sb.append(w);
                lineLength += w.length();
            }
            else if (lineLength + w.length() + 1 <= this.limit) {
                // word does not overflow line
                sb.append(' ' + w);
                lineLength += w.length() + 1;
            }
            else {
                // word overflows line
                lines.add(sb.toString());
                sb.setLength(0);
                sb.append(w);
                lineLength = w.length();
            }
        }
        // add last built string to the list and return
        lines.add(sb.toString());
        return lines;
    }
}
