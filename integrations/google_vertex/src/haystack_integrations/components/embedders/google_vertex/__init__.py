# SPDX-FileCopyrightText: 2023-present deepset GmbH <info@deepset.ai>
#
# SPDX-License-Identifier: Apache-2.0
from .document_embedder import VertexAIDocumentEmbedder
from .text_embedder import VertexAITextEmbedder

__all__ = ["VertexAIDocumentEmbedder", "VertexAITextEmbedder"]
