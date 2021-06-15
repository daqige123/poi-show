from neo4j import GraphDatabase


class Graph:

    # node label, node weight, node name, relation label, relation weight, orientation
    def set_properties(self, nl, nw, nn, rl):
        self.nl = nl
        self.nn = nn
        self.rl = rl


    def get_nodes(self):
        graph = Graph("bolt://localhost:11012", username="neo4j", password="daqige666")
        ret = graph.run('match(p:POI) return p').data()
        print(ret[:2])
        result = []
        return ret

    def get_relationships(self):
        cmd = "MATCH (a:$nl) -[r:$rl]-> (b:$nl) RETURN *"
        cmd = cmd.replace("$nl", self.nl).replace("$rl", self.rl)
        with self._driver.session() as session:
            rel = session.write_transaction(self._run, cmd)

            result = []
            for i in rel:
                node1 = i['a']
                node2 = i['b']
                rel = i['r']
                result.append({
                    'id': rel.id,
                    'source': str(node1.id),
                    'sourcename': str(node1[self.nn]),
                    'target': str(node2.id),
                    'targetname': str(node2[self.nn]),
                    'weight': rel[self.rw]
                })
            return result

    @staticmethod
    def _run(tx, cmd):
        return tx.run(cmd)

if __name__ == "__main__":
    a = Graph("bolt://localhost:10012", "neo4j", "daqige666")
    a.close()