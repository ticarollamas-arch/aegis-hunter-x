import React, { useState, useEffect } from 'react';

export default function Dashboard() {
  const [logs, setLogs] = useState([
    { id: 1, payload: 'SELECT * FROM users WHERE id = 1', score: 85, status: 'BLOCKED', time: '10:42:15' },
    { id: 2, payload: 'GET /api/v1/health', score: 0, status: 'ALLOWED', time: '10:43:01' },
    { id: 3, payload: '../etc/passwd', score: 95, status: 'BLOCKED', time: '10:45:12' }
  ]);

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 font-sans p-8">
      <header className="border-b border-slate-800 pb-6 mb-8 flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold tracking-tight text-emerald-400">AEGIS HUNTER-X</h1>
          <p className="text-slate-400 text-sm mt-1">Enterprise Security Hub & AI Agent Monitor</p>
        </div>
        <div className="flex gap-4">
          <span className="px-3 py-1 bg-emerald-950 text-emerald-400 border border-emerald-800 rounded-full text-xs font-semibold flex items-center gap-2">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            SISTEMA ATIVO
          </span>
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div className="bg-slate-900/50 border border-slate-800 rounded-xl p-6 backdrop-blur-md">
          <h3 className="text-slate-400 text-xs font-semibold uppercase tracking-wider">Total de Requisições</h3>
          <p className="text-4xl font-bold mt-2 text-white">1,248</p>
        </div>
        <div className="bg-slate-900/50 border border-slate-800 rounded-xl p-6 backdrop-blur-md">
          <h3 className="text-slate-400 text-xs font-semibold uppercase tracking-wider">Ataques Bloqueados</h3>
          <p className="text-4xl font-bold mt-2 text-rose-500">42</p>
        </div>
        <div className="bg-slate-900/50 border border-slate-800 rounded-xl p-6 backdrop-blur-md">
          <h3 className="text-slate-400 text-xs font-semibold uppercase tracking-wider">Média de Risco</h3>
          <p className="text-4xl font-bold mt-2 text-amber-400">12.4%</p>
        </div>
      </div>

      <div className="bg-slate-900/30 border border-slate-800 rounded-xl overflow-hidden">
        <div className="px-6 py-4 border-b border-slate-800 bg-slate-900/80 flex justify-between items-center">
          <h2 className="font-semibold text-slate-200">Console de Auditoria em Tempo Real</h2>
          <button className="text-xs text-emerald-400 hover:underline">Limpar Logs</button>
        </div>
        <div className="divide-y divide-slate-800/60">
          {logs.map((log) => (
            <div key={log.id} className="px-6 py-4 flex items-center justify-between hover:bg-slate-900/20 transition-colors">
              <div className="flex items-center gap-4">
                <span className={`px-2 py-1 rounded text-xs font-mono font-bold ${
                  log.status === 'BLOCKED' ? 'bg-rose-950 text-rose-400 border border-rose-800' : 'bg-emerald-950 text-emerald-400 border border-emerald-800'
                }`}>
                  {log.status}
                </span>
                <div>
                  <p className="font-mono text-sm text-slate-300">{log.payload}</p>
                  <span className="text-xs text-slate-500">{log.time}</span>
                </div>
              </div>
              <div className="text-right">
                <span className="text-xs text-slate-400 block">Score de Risco</span>
                <span className={`font-bold ${log.score > 50 ? 'text-rose-400' : 'text-emerald-400'}`}>{log.score}%</span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}