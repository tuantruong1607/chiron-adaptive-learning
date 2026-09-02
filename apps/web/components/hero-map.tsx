"use client";

import { motion, useReducedMotion } from "motion/react";
import { concepts, edges } from "@/lib/demo-data";

export function HeroMap() {
  const reduce = useReducedMotion();
  const lookup = Object.fromEntries(
    concepts.map((concept) => [concept.id, concept]),
  );
  return (
    <div className="hero-map" aria-label="Bản đồ kiến thức đang hoạt động">
      <svg
        className="map-lines"
        viewBox="0 0 100 88"
        preserveAspectRatio="none"
        aria-hidden="true"
      >
        {edges.map((edge) => {
          const source = lookup[edge.source];
          const target = lookup[edge.target];
          return (
            <line
              key={edge.id}
              x1={source.x}
              y1={source.y}
              x2={target.x}
              y2={target.y}
            />
          );
        })}
      </svg>
      {concepts.map((concept, index) => (
        <motion.div
          className={`hero-node node-${concept.band}`}
          key={concept.id}
          style={{ left: `${concept.x}%`, top: `${concept.y}%` }}
          initial={reduce ? false : { opacity: 0, scale: 0.7 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{
            delay: index * 0.07,
            type: "spring",
            stiffness: 110,
            damping: 18,
          }}
        >
          <span>{concept.name}</span>
          <strong>{Math.round(concept.mastery * 100)}%</strong>
        </motion.div>
      ))}
      <div className="map-caption glass-surface">
        <span>Ưu tiên hiện tại</span>
        <strong>RAG evaluation</strong>
      </div>
    </div>
  );
}
