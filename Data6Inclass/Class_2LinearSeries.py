{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNxXrddYlaeYWEcsTAppsgs",
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
        "<a href=\"https://colab.research.google.com/github/nittayac/DFEDATA6-EX1/blob/main/Data6Inclass/Class_2LinearSeries.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
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
        "id": "Jgw0A1ytNC6c"
      },
      "execution_count": null,
      "outputs": []
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
        "outputId": "43790bd8-19a6-4615-ea3a-cd059a2a8d06"
      },
      "execution_count": 19,
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
        "%%writefile Data6Inclass/Class_2LinearSeries.py\n",
        "\n",
        "class LinearSeries:\n",
        "  def __iter__(self):\n",
        "    self.num = 1 # starting point\n",
        "    return self\n",
        "  def __next__(self):\n",
        "    self.num = self.num + 1 # how to calculate the next element\n",
        "    return self.num"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9Z6fgNh2Qfuh",
        "outputId": "7da55628-eb88-41ea-f66b-e116c23be7f5"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Appending to Data6Inclass/Class_2LinearSeries.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile -a Data6Inclass/Class_2LinearSeries.py\n",
        "# or\n",
        "#class LinearSeries:\n",
        "#  def __iter__(self):\n",
        "#    self.num = 0 # starting point\n",
        "#    return self\n",
        "#  def __next__(self):\n",
        "#    self.num = self.num + 1 # how to calculate the next element\n",
        "#    return self.num"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4NBU7gGjQzOc",
        "outputId": "22014320-34f1-4481-9e10-e0bb9715e7df"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Appending to Data6Inclass/Class_2LinearSeries.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile -a Data6Inclass/Class_2LinearSeries.py\n",
        "\n",
        "myseries = LinearSeries()\n",
        "randompointer = iter(myseries)\n",
        "\n",
        "\n",
        "# the starting point of series\n",
        "next(randompointer)\n",
        "next(randompointer)\n",
        "next(randompointer)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QwsLpvU_RTwd",
        "outputId": "94adab05-0808-4d65-d4fc-d7c88565d4c2"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Appending to Data6Inclass/Class_2LinearSeries.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile -a Data6Inclass/Class_2LinearSeries.py\n",
        "\n",
        "#or use for\n",
        "for i in range(10):\n",
        "  print(next(randompointer))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FO-ceRMrRff0",
        "outputId": "8707e9e3-06b2-4a67-cd26-d0bc25aa7765"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Appending to Data6Inclass/Class_2LinearSeries.py\n"
          ]
        }
      ]
    }
  ]
}