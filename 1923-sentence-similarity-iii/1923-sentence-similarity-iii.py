class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Command 1: Split both input strings into lists of words
        sentence1 = sentence1.split(" ")
        sentence2 = sentence2.split(" ")

        # Command 2: If both sentences are identical, return True immediately
        if sentence1 == sentence2: return True

        # Command 3: Initialize empty lists for common prefixes and suffixes
        # Also get the lengths of both sentences for easier reference
        prefix, suffix = [], []
        n, m = len(sentence1), len(sentence2)

        # Command 4: Find common prefix (matching words from the beginning)
        for i in range(min(n, m)):
            if sentence1[i] == sentence2[i]:
                prefix.append(sentence1[i])
            else:
                break
        
        # Command 5: Find common suffix (matching words from the end)
        for i in range(min(len(sentence1), len(sentence2))):
            if sentence1[n - i - 1] == sentence2[m - i - 1]:
                suffix.append(sentence1[n - i - 1])
            else:
                break

        # Command 6: Reverse the suffix to get correct word order
        suffix.reverse()        

        # Command 7: Handle overlap between prefix and suffix
        # If combined length is greater than shorter sentence,
        # there might be overlap
        while len(suffix) + len(prefix) > min(n, m):
            if suffix[0] == prefix[-1]:
                prefix.pop()

        # Command 8: Combine prefix and suffix into one list
        prefix.extend(suffix)

        # Command 9: Check if the combined prefix+suffix equals either original sentence
        return prefix == sentence1 or prefix == sentence2
        