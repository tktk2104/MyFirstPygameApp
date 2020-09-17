
class GameObjectManager:

    #<
    def __init__(self):

        self.gameobjects    = []    # ゲームオブジェクトのリスト
    #>


    #<
    # 引数のオブジェクトを管理リストに追加する
    def add(self, newObject):

        self.gameobjects.append(newObject)

        self.gameobjects.sort(key = lambda x:x.drawPriority)
    #>


    #<
    # オブジェクト名から対応するオブジェクトのリストを取得する
    def findGameObjectsWithName(self, name):

        result = []

        for gameObject in self.gameobjects:

            if gameObject.getName() == name:
                result.append(gameObject)

        return result
    #>


    #<
    # ゲームオーバー判定
    def isGameOver(self):

        return not self.findGameObjectsWithName("Player")
    #>


    #<
    # 全てのゲームオブジェクトの更新処理を呼ぶ
    def update(self):

        self.gameobjects = [object for object in self.gameobjects if not object.isDead]

        for gameobject in self.gameobjects:
            gameobject.update()
    #>


    #<
    # 全てのゲームオブジェクトの描画処理を呼ぶ
    def draw(self):

        for gameobject in self.gameobjects:
            gameobject.draw()
    #>


    