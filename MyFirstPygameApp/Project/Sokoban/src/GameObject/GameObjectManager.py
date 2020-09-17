
class GameObjectManager:

    #<
    def __init__(self):

        self.gameobjects = []   # ゲームオブジェクトのリスト
        self.goalObjects = []   # ゴールオブジェクトのリスト
    #>


    #<
    # 引数のオブジェクトを管理リストに追加する
    def add(self, newObject):

        self.gameobjects.append(newObject)

        self.gameobjects.sort(key = lambda x:x.drawPriority)

        if newObject.getName() == "Goal":
             self.goalObjects.append(newObject)
    #>


    #<
    # マス目座標から対応するオブジェクトのリストを取得する
    def findGameObjectsWithGridPos(self, x, y):

        result = []

        for gameObject in self.gameobjects:

            tempPos = gameObject.getGridPos()
            if tempPos[0] == x and tempPos[1] == y:
                result.append(gameObject)

        return result
    #>


    #<
    # ゲームクリア判定
    def isGameClear(self):

        for goalObject in self.goalObjects:

             if not goalObject.onBox:

                 return False

        return True
    #>


    #<
    # 全てのゲームオブジェクトの更新処理を呼ぶ
    def update(self):

        for gameobject in self.gameobjects:
            gameobject.update()
    #>


    #<
    # 全てのゲームオブジェクトの描画処理を呼ぶ
    def draw(self):

        for gameobject in self.gameobjects:
            gameobject.draw()
    #>


    