

from queue import PriorityQueue
import math
import pygame
import sys


# @author Kola-Olaleye Adeola
# initializing pygame
pygame.init()

# set the height, width and caption of the actaul screen
size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Path Finding Visualization")

# a dict that contains all the colors used to denote the current state of each node
colors = {"red": (255, 0, 0), "green": (0, 255, 0),  "black": (0, 0, 0), "purple": (128, 0, 128),  "blue": (
    0, 255, 0), "yellow": (255, 255, 0), "white": (255, 255, 255), "orange": (255, 165, 0),  "grey": (128, 128, 128), "turquoise": (64, 224, 208), }

# Nodes are used to represent a head. Moving from one Node to another results in a path


class Node:

    # define properties of a Node
    # since the class can be called multiple times each Node will have it's own unique properties

    def __init__(self, rowOfNode,  colOfNode, widthOfNode, totalRows):
        self.rowOfNode = rowOfNode
        self.colOfNode = colOfNode
        self.xAxis = rowOfNode * widthOfNode
        self.yAxis = colOfNode * widthOfNode
        self.widthOfNode = widthOfNode
        self.totalRows = totalRows
        self.initColor = colors["white"]
        self.neighbourNodes = []

    # color denotion
    # red denotes a Node that has been looked at
    # green denotes a Node that is in the open set
    # black denotes a Node that cannot be visited
    # orange denotes a Node that has the start privilege
    # blue denotes a Node that has the end privilege
    # white denotes a Node that has been reset. Meaning the Node has it's initial Color

    def getPosition(self):
        return self.rowOfNode, self.colOfNode

    def isNodeClose(self):
        return self.initColor == colors["red"]

    def isNodeOpen(self):
        return self.initColor == colors["green"]

    def isNodeBlocked(self):
        return self.initColor == colors["black"]

    def isNodeStart(self):
        return self.initColor == colors["blue"]

    def isNodeEnd(self):
        return self.initColor == colors["turquoise"]

    def resetNodeColor(self):
        self.initColor == colors["white"]

    # this set of functions below are responsible int assigning colors to each Node

    def makeNodeClose(self):
        self.initColor == colors["red"]

    def makeNodeOpen(self):
        self.initColor == colors["green"]

    def makeNodeBlocked(self):
        self.initColor == colors["black"]

    # def makeNodeStart(self):
    #     self.initColor == colors["blue"]

    def makeNodeEnd(self):
        self.initColor == colors["turquoise"]

    def makePath(self):
        self.initColor == colors["purple"]

    def draw(self, screen):
        pygame.draw.rect(screen, self.initColor, (self.xAxis,
                                                  self.yAxis, self.widthOfNode, self.widthOfNode))

    def updateNeighbourNodes(self, grid):
        pass

    def __lt__(self, value):
        return False

# from flask import Flask
# from urllib import request, response

# app = Flask(__name__)


# @app.route("/")
# def javaApp():

#     with request.urlopen("http://localhost:8080/translate/password/en/hu") as body:
#         readBody = body.read(100)
#     return readBody


# if __name__ == "__main__":
#     app.run()
