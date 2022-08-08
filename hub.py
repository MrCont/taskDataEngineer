import DevOps1 as dv


class chad_list(dv.lista):
    def __init__(self) -> None:
        super().__init__()

    def delete(self):
        del self.numb
        self.numb = []

    def set_list(self, new_value: list) -> None:
        self.delete()
        self.numb = new_value

    def __repr__(self):
        return str(self.numb)


if __name__ == "__main__":
    a = chad_list()
    a.set_list([1,4,3,2])
    print(a)
    a.reverse()
    print(a)