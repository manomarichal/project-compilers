

class Visitor:
    def visit(self, node):
        return node.accept(self)

    def visitComposite(self, node):
        return self.visitChildren(node)

    def visitChildren(self, node):
        result = self.defaultResult()
        n = node.get_child_count()
        for i in range(n):
            if not self.shouldVisitNextChild(node, result):
                return result

            c = node.get_child(i)
            childResult = c.accept(self)
            result = self.aggregateResult(result, childResult)

        return result

    def defaultResult(self):
        return None

    def aggregateResult(self, aggregate, nextResult):
        if nextResult is None:
            return aggregate
        if aggregate is None:
            return [nextResult]
        aggregate.append(nextResult)
        return aggregate

    def shouldVisitNextChild(self, node, currentResult):
        return True
