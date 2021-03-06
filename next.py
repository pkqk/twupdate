import os

def state():
    try:
      with open('state') as f:
          return f.read()
    except IOError:
      return images()[0]

def images():
    return os.listdir('images')

def next(state, images):
    n = images.index(state)
    n = (n + 1) % len(images)
    return images[n]

def save(state):
    with open('state', 'w') as f:
        f.write(state)

if __name__ == "__main__":
    n = next(state(), images())
    save(n)
    print n
