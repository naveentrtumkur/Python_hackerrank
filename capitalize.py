/*

You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.



Given a full name, your task is to capitalize the name appropriately.

*/

a_string = input().split(' ') 
print(' '.join((word.capitalize() for word in a_string))) 
