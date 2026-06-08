# Generated from C:/Users/Ismael/Documents/Semestres/V semestre/Compiladores e interpretes/Proyecto final/MiniGoCompiler/MiniGo.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#root.
    def visitRoot(self, ctx:MiniGoParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#topDeclarationList.
    def visitTopDeclarationList(self, ctx:MiniGoParser.TopDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#variableDecl.
    def visitVariableDecl(self, ctx:MiniGoParser.VariableDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#innerVarDecls.
    def visitInnerVarDecls(self, ctx:MiniGoParser.InnerVarDeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#singleVarDecl.
    def visitSingleVarDecl(self, ctx:MiniGoParser.SingleVarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#singleVarDeclNoExps.
    def visitSingleVarDeclNoExps(self, ctx:MiniGoParser.SingleVarDeclNoExpsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typeDecl.
    def visitTypeDecl(self, ctx:MiniGoParser.TypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#innerTypeDecls.
    def visitInnerTypeDecls(self, ctx:MiniGoParser.InnerTypeDeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#singleTypeDecl.
    def visitSingleTypeDecl(self, ctx:MiniGoParser.SingleTypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcDecl.
    def visitFuncDecl(self, ctx:MiniGoParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcFrontDecl.
    def visitFuncFrontDecl(self, ctx:MiniGoParser.FuncFrontDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcArgDecls.
    def visitFuncArgDecls(self, ctx:MiniGoParser.FuncArgDeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declType.
    def visitDeclType(self, ctx:MiniGoParser.DeclTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#sliceDeclType.
    def visitSliceDeclType(self, ctx:MiniGoParser.SliceDeclTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayDeclType.
    def visitArrayDeclType(self, ctx:MiniGoParser.ArrayDeclTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structDeclType.
    def visitStructDeclType(self, ctx:MiniGoParser.StructDeclTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structMemDecls.
    def visitStructMemDecls(self, ctx:MiniGoParser.StructMemDeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#identifierList.
    def visitIdentifierList(self, ctx:MiniGoParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expressionList.
    def visitExpressionList(self, ctx:MiniGoParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unaryMinusExpression.
    def visitUnaryMinusExpression(self, ctx:MiniGoParser.UnaryMinusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unaryBitNotExpression.
    def visitUnaryBitNotExpression(self, ctx:MiniGoParser.UnaryBitNotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unaryPlusExpression.
    def visitUnaryPlusExpression(self, ctx:MiniGoParser.UnaryPlusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unaryNotExpression.
    def visitUnaryNotExpression(self, ctx:MiniGoParser.UnaryNotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:MiniGoParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primaryExpressionOnly.
    def visitPrimaryExpressionOnly(self, ctx:MiniGoParser.PrimaryExpressionOnlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#relationalExpression.
    def visitRelationalExpression(self, ctx:MiniGoParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:MiniGoParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:MiniGoParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:MiniGoParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#multiplicativeOp.
    def visitMultiplicativeOp(self, ctx:MiniGoParser.MultiplicativeOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#additiveOp.
    def visitAdditiveOp(self, ctx:MiniGoParser.AdditiveOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#relationalOp.
    def visitRelationalOp(self, ctx:MiniGoParser.RelationalOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:MiniGoParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#operand.
    def visitOperand(self, ctx:MiniGoParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#index.
    def visitIndex(self, ctx:MiniGoParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arguments.
    def visitArguments(self, ctx:MiniGoParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#selector.
    def visitSelector(self, ctx:MiniGoParser.SelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#appendExpression.
    def visitAppendExpression(self, ctx:MiniGoParser.AppendExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lengthExpression.
    def visitLengthExpression(self, ctx:MiniGoParser.LengthExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#capExpression.
    def visitCapExpression(self, ctx:MiniGoParser.CapExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statementList.
    def visitStatementList(self, ctx:MiniGoParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block.
    def visitBlock(self, ctx:MiniGoParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#simpleStatement.
    def visitSimpleStatement(self, ctx:MiniGoParser.SimpleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#nonEmptySimpleStatement.
    def visitNonEmptySimpleStatement(self, ctx:MiniGoParser.NonEmptySimpleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:MiniGoParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignmentOp.
    def visitAssignmentOp(self, ctx:MiniGoParser.AssignmentOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifStatement.
    def visitIfStatement(self, ctx:MiniGoParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#loop.
    def visitLoop(self, ctx:MiniGoParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#switchStmt.
    def visitSwitchStmt(self, ctx:MiniGoParser.SwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expressionCaseClauseList.
    def visitExpressionCaseClauseList(self, ctx:MiniGoParser.ExpressionCaseClauseListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expressionCaseClause.
    def visitExpressionCaseClause(self, ctx:MiniGoParser.ExpressionCaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expressionSwitchCase.
    def visitExpressionSwitchCase(self, ctx:MiniGoParser.ExpressionSwitchCaseContext):
        return self.visitChildren(ctx)



del MiniGoParser