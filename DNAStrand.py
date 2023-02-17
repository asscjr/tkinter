#!/usr/bin/env python
# coding: UTF-8
#
## @package DNAStrand
#
#   Playing with string matching.
#
#   @author Paulo Roma
#   @since 15/12/2019
#   @see https://www.sciencedirect.com/topics/medicine-and-dentistry/dna-strand
#
import sys

class DNAStrand:

    ## Valid DNA symbols.
    symbols = 'ATCG'

    ##
     # Constructs a DNAStrand with the given string of data, 
     # normally consisting of characters 'A', 'C', 'G', and 'T'.
     # Raises a ValueError exception, in case of an invalid givenData strand.
     #
     # @param givenData string of characters for this DNAStrand.
     #
    def __init__(self, givenData):
        ## Strand of this DNA, in upper case.
        self.strand = givenData.upper()

        # ...
        #Condition that raises a ERROR if the strand is not a DNA strand.
        if not self.isValid():
            raise Exception ("Invalid givenData strand")


    ## Returns a string representing the strand data of this DNAStrand.
    def __repr__(self):
        return self.strand


    ##
     # Returns a new DNAStrand that is the complement of this one,
     # that is, 'A' is replaced with 'T' and so on.
     #
     # @return complement of this DNA.
     #
    def createComplement(self):
        complement = ""

        # ....
        #For each letter in the strand it substitutes for it's pair base, creating a complement of the strand.
        for ch in self.strand:
            if ch == "A":
                complement += "T"
            elif ch == "T":
                complement += "A"
            elif ch == "C":
                complement += "G"
            else:
                complement += "C"

        
        return DNAStrand(complement)
    

    ##
     # Returns a string showing which characters in this strand are matched
     #  with 'other', when shifted left by the given amount.
     #
     # @param other given DNAStrand.
     # @param shift number of positions to shift other to the left.
     # @return a copy of this strand, where matched characters are upper case 
     #         and unmatched, lower case.
     #

    #Eu utilizei o gabarito e modifiquei esse método para melhor funcionamento do código da AD2
    def findMatchesWithLeftShift(self, other, shift):
        local = (len(other.strand) - shift)
        if (local <= 0):
            return self.strand.lower()
        shortest = min(local, len(self.strand))
        matches = ""

        for i in range(shortest):
            c = self.strand[i]
            matches += c if self.match(c, other.strand[shift + i]) else c.lower()

        temp = self.strand.lower()
        matches = matches + temp[shortest:]
        matches += temp[len(matches) : len(self.strand)]
        assert(len(matches) == len(self.strand))
    
        return matches
    

    ##
     # Returns a string showing which characters in this strand are matched 
     # with 'other', when shifted right by the given amount.
     #
     # @param other given DNAStrand.
     # @param shift number of positions to shift other to the right.
     # @return a copy of this strand, where matched characters are upper case 
     #         and unmatched, lower case.
     #

    #Eu utilizei o gabarito e modifiquei esse método para melhor funcionamento do código da AD2
    def findMatchesWithRightShift(self, other, shift):
        local = (len(self.strand) - shift)
        if (local <= 0):
            return self.strand.lower()
        shortest = min(local, len(other.strand))
        matches = ""

        for i in range(shortest):
            c = self.strand[shift + i]
            matches += c if self.match(c, other.strand[i]) else c.lower()

        temp = self.strand.lower()
        matches = temp[:shift] + matches
        matches += temp[len(matches) : len(self.strand)]
        assert(len(matches) == len(self.strand))
    
        return matches

    ##
     # Returns the maximum possible number of matching base pairs,
     # when the given sequence is shifted left or right by any amount.
     #
     # @param other given DNAStrand to be matched with this one.
     # @return maximum number of matching pairs.
     #

    #Eu utilizei o gabarito e modifiquei esse método para melhor funcionamento do código da AD2
    def findMaxPossibleMatches(self, other):
        direction = ""
        greater = self.countMatchesWithLeftShift(other, 0)
        pos = 0
        for shift in range(1, len(self.strand)):
            if self.countMatchesWithLeftShift(other, shift) > greater:
                greater = self.countMatchesWithLeftShift(other, shift)
                pos = shift
                direction = "right"
        for shift in range(1, len(self.strand)):
            if self.countMatchesWithRightShift(other, shift) > greater:
                greater = self.countMatchesWithRightShift(other, shift)
                pos = shift
                direction = "left"
        return pos, direction
    

    ##
     # Returns the number of matching pairs,
     # when 'other' is shifted to the left by 'shift' positions.
     #
     # @param other given DNAStrand to match with this strand.
     # @param shift number of positions to shift other to the left.
     # @return number of matching pairs.
     #

    #Eu utilizei o gabarito e modifiquei esse método para melhor funcionamento do código da AD2
    def countMatchesWithLeftShift(self, other, shift):
        local = (len(other.strand) - shift)
        if (local <= 0):
            return 0
        shortest = min(local, len(self.strand))
        count = 0

        for i in range(shortest):
            c = self.strand[i]
            if self.match(c, other.strand[shift + i]):
                count += 1 
        
        return count
    

    ##
     # Returns the number of matching pairs,
     # when 'other' is shifted to the right by 'shift' positions.
     #
     # @param other given DNAStrand to be matched with this one.
     # @param shift number of positions to shift other to the right.
     # @return number of matching pairs.
     #

    #Eu utilizei o gabarito e modifiquei esse método para melhor funcionamento do código da AD2
    def countMatchesWithRightShift (self, other, shift):
        local = (len(self.strand) - shift)
        if (local <= 0):
            return 0
        shortest = min(local, len(other.strand))
        count = 0

        for i in range(shortest):
            c = self.strand[shift + i]
            if self.match(c, other.strand[i]):
                count += 1 

        
        return count
    

    ##
     # Determines whether all characters in this strand 
     # are valid ('A', 'G', 'C', or 'T').
     #
     # @return True if valid, and False otherwise.
     #
    def isValid(self):
        valid = True

        # ...
        #Loop with conditions to make sure the strand given is a DNA strand.
        for ch in self.strand:
            if ch != "A":
                if ch != "T":
                    if ch != "G":
                        if ch != "C":
                            valid = False
        
        return valid
    

    ##
     # Counts the number of occurrences of the given character in this strand.
     #
     # @param ch given character.
     # @return number of occurrences of ch.
     #
    def letterCount(self,ch):
        count = 0

        # ...
        #Loop to count how many times a character happens in a strand.
        for char in self.strand:
            if char == ch:
                count += 1
        
        return count
    

    ##
     # Returns True if the two characters form a base pair 
     # ('A' with 'T' or 'C' with 'G').
     #
     # @param c1 first character.
     # @param c2 second character.
     # @return True if they form a base pair, and False otherwise.
     #
    def match(self, c1, c2):
        match = False

        # ...
        #Condition to know if a pair of two characters is a pair base.
        if (c1 == "A" and c2 == "T") or (c1 == "T" and c2 == "A") or (c1 == "C" and c2 == "G") or (c1 == "G" and c2 == "C"):
            match = True
 
        return match