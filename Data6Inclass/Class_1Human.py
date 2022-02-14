{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOrwYFFP6RE/bQHW2CJGbsj",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/nittayac/DFEDATA6-EX1/blob/main/Data6Inclass/Class_1Human.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9NffgHeiMfzi",
        "outputId": "cd04f865-83f5-4e50-a1e0-fb9c34bbb8c3"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting Data6Inclass/Class_1Human.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile Data6Inclass/Class_1Human.py\n",
        "# Geographic point-> lati, long\n",
        "# a,b -> remember 2 names; operate on 2 names\n",
        "# CLASS \n",
        "\n",
        "# functional-> functions\n",
        "# how to do things\n",
        "# 1. Switch on the fan _ def fan_on():\n",
        "# 2. change the speed def change_speed():\n",
        "# 3. switch off the fan def fan_off():\n",
        "\n",
        "# Objected oriented-> classes \n",
        "# IDENTIFY-> NOUN, VERBS\n",
        "# CLASS FAN-> can perform 3 functions\n",
        "# class Fan:\n",
        "# def switch_on, change_speed, switch_off\n",
        "# Fan f1; f1.on(). \n",
        "# OBJECTS\n",
        "\n",
        "class Human:\n",
        "  def speak(this):\n",
        "    print('bye bye')\n",
        "  def jump(this):\n",
        "    return \"i jumped. Bye bye.\"\n",
        "  def eat(this, food):\n",
        "    return food-1"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "LLWcErzUMzJ3"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile -a Data6Inclass/Class_1Human.py\n",
        "\n",
        "\n",
        "#Human-> 1 nose\n",
        "# 3 noses;\n",
        "class Human:\n",
        "  def __init__(self): # called automatically \n",
        "    self.noseCount = 1\n",
        "    self.tailCount = 0\n",
        "  def getLimbCount(self):\n",
        "    print('Nose count = ' + str(self.noseCount))\n",
        "    print('Tail count = ' + str(self.tailCount))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u3t49dyPM2NY",
        "outputId": "285be483-9955-4b51-a48d-80a309ef0484"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Appending to Data6Inclass/Class_1Human.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile -a Data6Inclass/Class_1Human.py\n",
        "\n",
        "john = Human()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VHJQWOGMM3jV",
        "outputId": "7f34b3cb-aa26-411d-9e0d-1022e04ffc9d"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Appending to Data6Inclass/Class_1Human.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile -a Data6Inclass/Class_1Human.py\n",
        "\n",
        "print(dir(john))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iDcih6E9M_NO",
        "outputId": "5b198760-c6e5-4bce-8be2-745ed4ad1e26"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Appending to Data6Inclass/Class_1Human.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dir(john)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Jgw0A1ytNC6c",
        "outputId": "97cf9a51-4e92-4de1-d8be-dbcef9f565b3"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['__class__',\n",
              " '__delattr__',\n",
              " '__dict__',\n",
              " '__dir__',\n",
              " '__doc__',\n",
              " '__eq__',\n",
              " '__format__',\n",
              " '__ge__',\n",
              " '__getattribute__',\n",
              " '__gt__',\n",
              " '__hash__',\n",
              " '__init__',\n",
              " '__init_subclass__',\n",
              " '__le__',\n",
              " '__lt__',\n",
              " '__module__',\n",
              " '__ne__',\n",
              " '__new__',\n",
              " '__reduce__',\n",
              " '__reduce_ex__',\n",
              " '__repr__',\n",
              " '__setattr__',\n",
              " '__sizeof__',\n",
              " '__str__',\n",
              " '__subclasshook__',\n",
              " '__weakref__',\n",
              " 'getLimbCount',\n",
              " 'noseCount',\n",
              " 'tailCount']"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile -a Data6Inclass/Class_1Human.py\n",
        "\n",
        "john.getLimbCount()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KO4u47NnNGHe",
        "outputId": "94440855-4ce8-4f12-c137-98b003b7ae44"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Appending to Data6Inclass/Class_1Human.py\n"
          ]
        }
      ]
    }
  ]
}