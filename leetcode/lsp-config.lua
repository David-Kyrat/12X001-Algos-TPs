{ {
    _on_attach = <function 1>,
    attached_buffers = { true },
    cancel_request = <function 2>,
    commands = {},
    config = {
      autostart = true,
      capabilities = {
        textDocument = <1>{
          callHierarchy = {
            dynamicRegistration = false
          },
          codeAction = {
            codeActionLiteralSupport = {
              codeActionKind = {
                valueSet = { "", "quickfix", "refactor", "refactor.extract", "refactor.inline", "refactor.rewrite", "source", "source.organizeImports" }
              }
            },
            dataSupport = true,
            dynamicRegistration = false,
            isPreferredSupport = true,
            resolveSupport = {
              properties = { "edit" }
            }
          },
          completion = {
            completionItem = {
              commitCharactersSupport = true,
              deprecatedSupport = true,
              documentationFormat = { "markdown", "plaintext" },
              insertReplaceSupport = true,
              insertTextModeSupport = {
                valueSet = { 1, 2 }
              },
              labelDetailsSupport = true,
              preselectSupport = true,
              resolveSupport = {
                properties = { "documentation", "detail", "additionalTextEdits", "sortText", "filterText", "insertText", "textEdit", "insertTextFormat", "insertTextMode" }
              },
              snippetSupport = true,
              tagSupport = {
                valueSet = { 1 }
              }
            },
            completionItemKind = {
              valueSet = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25 }
            },
            completionList = {
              itemDefaults = { "commitCharacters", "editRange", "insertTextFormat", "insertTextMode", "data" }
            },
            contextSupport = true,
            dynamicRegistration = false,
            insertTextMode = 1
          },
          declaration = {
            linkSupport = true
          },
          definition = {
            linkSupport = true
          },
          documentHighlight = {
            dynamicRegistration = false
          },
          documentSymbol = {
            dynamicRegistration = false,
            hierarchicalDocumentSymbolSupport = true,
            symbolKind = {
              valueSet = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26 }
            }
          },
          hover = {
            contentFormat = { "markdown", "plaintext" },
            dynamicRegistration = false
          },
          implementation = {
            linkSupport = true
          },
          publishDiagnostics = {
            relatedInformation = true,
            tagSupport = {
              valueSet = { 1, 2 }
            }
          },
          references = {
            dynamicRegistration = false
          },
          rename = {
            dynamicRegistration = false,
            prepareSupport = true
          },
          semanticTokens = {
            augmentsSyntaxTokens = true,
            dynamicRegistration = false,
            formats = { "relative" },
            multilineTokenSupport = false,
            overlappingTokenSupport = true,
            requests = {
              full = {
                delta = true
              },
              range = false
            },
            serverCancelSupport = false,
            tokenModifiers = { "declaration", "definition", "readonly", "static", "deprecated", "abstract", "async", "modification", "documentation", "defaultLibrary" },
            tokenTypes = { "namespace", "type", "class", "enum", "interface", "struct", "typeParameter", "parameter", "variable", "property", "enumMember", "event", "function", "method", "macro", "keyword", "modifier", "comment", "string", "number", "regexp", "operator", "decorator" }
          },
          signatureHelp = {
            dynamicRegistration = false,
            signatureInformation = {
              activeParameterSupport = true,
              documentationFormat = { "markdown", "plaintext" },
              parameterInformation = {
                labelOffsetSupport = true
              }
            }
          },
          synchronization = {
            didSave = true,
            dynamicRegistration = false,
            willSave = true,
            willSaveWaitUntil = true
          },
          typeDefinition = {
            linkSupport = true
          }
        },
        window = <2>{
          showDocument = {
            support = true
          },
          showMessage = {
            messageActionItem = {
              additionalPropertiesSupport = false
            }
          },
          workDoneProgress = true
        },
        workspace = {
          applyEdit = true,
          configuration = true,
          didChangeWatchedFiles = <3>{
            dynamicRegistration = false,
            relativePatternSupport = true
          },
          semanticTokens = <4>{
            refreshSupport = true
          },
          symbol = <5>{
            dynamicRegistration = false,
            hierarchicalWorkspaceSymbolSupport = true,
            symbolKind = {
              valueSet = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26 }
            }
          },
          workspaceEdit = <6>{
            resourceOperations = { "rename", "create", "delete" }
          },
          workspaceFolders = true
        }
      },
      cmd = { "C:\\Users\\noahm\\AppData\\Local\\nvim-data\\mason\\bin\\ruff-lsp.CMD" },
      cmd_cwd = "C:/Users/noahm/DocumentsNb/BA3/Algo-TPs/leetcode",
      filetypes = { "python" },
      flags = {},
      get_language_id = <function 3>,
      handlers = <7>{},
      init_options = {
        settings = {
          args = { "--config=C:/Users/noahm/.config/pyproject.toml" }
        }
      },
      log_level = 2,
      message_level = 2,
      name = "ruff_lsp",
      on_attach = <function 4>,
      on_exit = <function 5>,
      on_init = <function 6>,
      root_dir = "C:/Users/noahm/DocumentsNb/BA3/Algo-TPs/leetcode",
      settings = {},
      single_file_support = true,
      workspace_folders = <8>{ {
          name = "C:/Users/noahm/DocumentsNb/BA3/Algo-TPs/leetcode",
          uri = "file:///C:/Users/noahm/DocumentsNb/BA3/Algo-TPs/leetcode"
        } },
      <metatable> = <9>{
        __tostring = <function 7>
      }
    },
    handlers = <table 7>,
    id = 1,
    initialized = true,
    is_stopped = <function 8>,
    messages = {
      messages = {},
      name = "ruff_lsp",
      progress = {},
      status = {}
    },
    name = "ruff_lsp",
    notify = <function 9>,
    offset_encoding = "utf-16",
    request = <function 10>,
    request_sync = <function 11>,
    requests = {},
    rpc = {
      is_closing = <function 12>,
      notify = <function 13>,
      request = <function 14>,
      terminate = <function 15>
    },
    server_capabilities = {
      codeActionProvider = {
        codeActionKinds = { "quickfix", "source.fixAll", "source.organizeImports", "source.fixAll.ruff", "source.organizeImports.ruff" },
        resolveProvider = true
      },
      executeCommandProvider = {
        commands = { "ruff.applyAutofix", "ruff.applyOrganizeImports" }
      },
      hoverProvider = true,
      textDocumentSync = {
        change = 2,
        openClose = true,
        save = true,
        willSave = false,
        willSaveWaitUntil = false
      },
      workspace = {
        fileOperations = vim.empty_dict(),
        workspaceFolders = {
          changeNotifications = true,
          supported = true
        }
      }
    },
    stop = <function 16>,
    supports_method = <function 17>,
    workspace_did_change_configuration = <function 18>,
    workspace_folders = <table 8>
  }, {
    _on_attach = <function 19>,
    attached_buffers = { true },
    cancel_request = <function 20>,
    commands = {},
    config = {
      autostart = true,
      capabilities = {
        textDocument = <table 1>,
        window = <table 2>,
        workspace = {
          applyEdit = true,
          configuration = true,
          didChangeWatchedFiles = <table 3>,
          semanticTokens = <table 4>,
          symbol = <table 5>,
          workspaceEdit = <table 6>,
          workspaceFolders = true
        }
      },
      cmd = { "C:\\Users\\noahm\\.python-venvs\\.venv_ds\\Scripts\\pyright-langserver.EXE", "--stdio", "-p C:/Users/noahm/.config/pyproject.toml" },
      cmd_cwd = "C:/Users/noahm/DocumentsNb/BA3/Algo-TPs/leetcode",
      filetypes = { "python" },
      flags = {},
      get_language_id = <function 21>,
      handlers = <table 7>,
      init_options = vim.empty_dict(),
      log_level = 2,
      message_level = 2,
      name = "pyright",
      on_attach = <function 22>,
      on_exit = <function 23>,
      on_init = <function 24>,
      root_dir = "C:/Users/noahm/DocumentsNb/BA3/Algo-TPs/leetcode",
      settings = {
        python = {
          analysis = {
            autoImportCompletions = false,
            autoSearchPaths = false,
            diagnosticMode = "file",
            useLibraryCodeForTypes = true
          }
        }
      },
      single_file_support = true,
      workspace_folders = <10>{ {
          name = "C:/Users/noahm/DocumentsNb/BA3/Algo-TPs/leetcode",
          uri = "file:///C:/Users/noahm/DocumentsNb/BA3/Algo-TPs/leetcode"
        } },
      <metatable> = <table 9>
    },
    handlers = <table 7>,
    id = 2,
    initialized = true,
    is_stopped = <function 25>,
    messages = {
      messages = {},
      name = "pyright",
      progress = {},
      status = {}
    },
    name = "pyright",
    notify = <function 26>,
    offset_encoding = "utf-16",
    request = <function 27>,
    request_sync = <function 28>,
    requests = {},
    rpc = {
      is_closing = <function 29>,
      notify = <function 30>,
      request = <function 31>,
      terminate = <function 32>
    },
    server_capabilities = {
      callHierarchyProvider = true,
      codeActionProvider = {
        codeActionKinds = { "quickfix", "source.organizeImports" },
        workDoneProgress = true
      },
      completionProvider = {
        completionItem = {
          labelDetailsSupport = true
        },
        resolveProvider = true,
        triggerCharacters = { ".", "[", '"', "'" },
        workDoneProgress = true
      },
      declarationProvider = {
        workDoneProgress = true
      },
      definitionProvider = {
        workDoneProgress = true
      },
      documentHighlightProvider = {
        workDoneProgress = true
      },
      documentSymbolProvider = {
        workDoneProgress = true
      },
      executeCommandProvider = {
        commands = {},
        workDoneProgress = true
      },
      hoverProvider = {
        workDoneProgress = true
      },
      referencesProvider = {
        workDoneProgress = true
      },
      renameProvider = {
        prepareProvider = true,
        workDoneProgress = true
      },
      signatureHelpProvider = {
        triggerCharacters = { "(", ",", ")" },
        workDoneProgress = true
      },
      textDocumentSync = {
        change = 2,
        openClose = true,
        save = {
          includeText = false
        },
        willSave = false,
        willSaveWaitUntil = false
      },
      typeDefinitionProvider = {
        workDoneProgress = true
      },
      workspace = {
        workspaceFolders = {
          changeNotifications = true,
          supported = true
        }
      },
      workspaceSymbolProvider = {
        workDoneProgress = true
      }
    },
    stop = <function 33>,
    supports_method = <function 34>,
    workspace_did_change_configuration = <function 35>,
    workspace_folders = <table 10>
  } }