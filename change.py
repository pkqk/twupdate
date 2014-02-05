import update
import next

def forward():
    n = next.next(next.state(), next.images())
    with open('images/%s' % n, 'rb') as f:
        update.profile_image(f)
    next.save(n)

if __name__ == "__main__":
    forward()
