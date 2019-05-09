#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Matematicas.

    Created on Thu May  9 16:15:17 2019
    
    @author: Marco Baturan
    @license: free
    @abstract: Program where I try to translate my mathematical studies.

"""


class Matricial:
    """Matricial.
    
        Class to instantiation for apply to POO style the
        methods of determinants of square second order matrix and
        rule of Sarrus for square third order matrix.
    
    """
    
    def __init__(self, matrix, sarrus):
        self.m = matrix
        self.s = sarrus
        
    def determinant(self):
        """Determinant.
        
            Function for calculate the determinants of square
            second order matrix.
            
        """
        a1 = self.m[0][0] * self.m[0][1]  # Product of a and b.
        a2 = self.m[1][0] * self.m[1][1]  # Product of c and d.
        a3 = a1 - a2                      # Substract of a1 and a2.
        print("The results is: ", a3)     # Print result.
    
    def sarrus_rule(self):
        """Sarrus rule.
            
            Procedure for get the determinant of square third order matrix.
            
        """
        a = self.s[0][0] * self.s[1][1] * self.s[2][2]  # Central diagonal.
        b = self.s[0][1] * self.s[1][2] * self.s[2][0]  # Second diagonal.
        c = self.s[0][2] * self.s[1][0] * self.s[2][1]  # Third diagonal.
        d = a + b + c                                   # Sum of a, b, c ops.
        print("The results is: ", d)                    # Print result.
